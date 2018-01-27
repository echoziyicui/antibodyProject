#!/usr/bin/perl -s
#*************************************************************************
#
#   Program:    clusterResidues
#   File:       clusterResidues.pl
#   
#   Version:    V1.1
#   Date:       16.06.15
#   Function:   Cluster residues having specified properties
#   
#   Copyright:  (c) Dr. Andrew C. R. Martin, UCL, 2015
#   Author:     Dr. Andrew C. R. Martin
#   Address:    Institute of Structural and Molecular Biology
#               Division of Biosciences
#               University College
#               Gower Street
#               London
#               WC1E 6BT
#   EMail:      andrew@bioinf.org.uk
#               
#*************************************************************************
#
#   This program is not in the public domain, but it may be copied
#   according to the conditions laid out in the accompanying file
#   COPYING.DOC
#
#   The code may be modified as required, but any modifications must be
#   documented so that the person responsible can be identified. If 
#   someone else breaks this code, I don't want to be blamed for code 
#   that does not work! 
#
#   The code may not be sold commercially or included as part of a 
#   commercial product except as described in the file COPYING.DOC.
#
#*************************************************************************
#
#   Description:
#   ============
#
#*************************************************************************
#
#   Usage:
#   ======
#
#*************************************************************************
#
#   Revision History:
#   =================
#   V1.0   15.04.15   Original   By: ACRM
#   V1.1   16.06.15   Added -m parameter
#
#*************************************************************************
# Add the path of the executable to the library path
#use FindBin;
#use lib $FindBin::Bin;
# Or if we have a bin directory and a lib directory
#use Cwd qw(abs_path);
#use FindBin;
#use lib abs_path("$FindBin::Bin/../lib");

use strict;

#*************************************************************************
$::distCut = (defined($::d)?$::d:8.5);       # Default 8.5
$::minResInCluster = (defined($::m)?$::m:0); # Default 0
UsageDie() if(defined($::h) || scalar(@ARGV) < 3);


#*************************************************************************
my $distanceMatrixFile = shift(@ARGV);
# Read the distance matrix data
my $hhDistanceMatrix = ReadDistanceMatrix($distanceMatrixFile);
Die($$hhDistanceMatrix{'ERROR'}) if(defined($$hhDistanceMatrix{'ERROR'}));
PrintDistanceMatrix($hhDistanceMatrix) if(defined($::v) && ($::v > 1));

# Take file/cutoff pairs from the command line
while(scalar(@ARGV))
{
    my $propertyFile = shift(@ARGV);
    UsageDie() if(!scalar(@ARGV)); # File but no cutoff
    my $cutoff = shift(@ARGV);

    # Read the file
    my %property = readTwoColumnHash($propertyFile);
    Die($property{'ERROR'}) if(defined($property{'ERROR'}));

    if(!defined($::q))
    {
        print STDERR "Retaining residues in $propertyFile with values $cutoff...\n";
    }

    # Filter on this property and print the new matrix
    FilterDistanceMatrix($hhDistanceMatrix, $cutoff, %property);
    PrintDistanceMatrix($hhDistanceMatrix) if(defined($::v));
}

# Finally run the clustering
RunClustering($hhDistanceMatrix, $::distCut, $::minResInCluster);


#*************************************************************************
#>RunClustering($hhDistanceMatrix, $distCut, $minResInCluster)
# ------------------------------------------------------------
# \param[in]  $hhDistanceMatrix - Ref to hash of hashes distance matrix
# \param[in]  $distCut          - Distance cutoff for clustering residues
# \param[in]  $minResInCluster  - Minimum residues in a cluster to bother
#                                 printing it (0 print all clusters)
# 
# This is the main routine that runs and prints the clustering results.
# It maintains a list of residues that are part of a cluster and steps
# through each residue not yet assigned to a cluster, calling the 
# recursive DoClustering() routine
# 
# 15.04.15 Original   By: ACRM
# 16.06.15 Added $minResInCluster
sub RunClustering
{
    my($hhDistanceMatrix, $distCut, $minResInCluster) = @_;

    # Initialize hash to say whether we have looked at clusters
    # involving each of the residues
    my %residues = ();
    foreach my $res (sort keys %$hhDistanceMatrix)
    {
        $residues{$res} = 0;
    }

    # Now look at clusters involving each residue in turn, if it
    # isn't already in a cluster
    my $clusterCount = 1;
    foreach my $res1 (sort keys %$hhDistanceMatrix)
    {
        if(!$residues{$res1})
        {
            my %cluster = ();
            my $clusterSize;

            %cluster = DoClustering($res1, $hhDistanceMatrix, $distCut, 
                                    %cluster);
            $clusterSize = scalar(keys %cluster);

            # Print members of the cluster and update the list of 
            # residues that have been assigned to a cluster
            if($clusterSize >= $minResInCluster)
            {
                printf "\nCluster %d\n", $clusterCount++;
            }
            foreach my $res2 (sort keys %cluster)
            {
                if($clusterSize >= $minResInCluster)
                {
                    print "$res2\n";
                }
                $residues{$res2} = 1;
            }
        }
    }
}

#*************************************************************************
#>%cluster = DoClustering($res, $hhDistanceMatrix, $distCut, %cluster)
# --------------------------------------------------------------------
# \param[in] $res              - First residue of cluster
# \param[in] $hhDistanceMatrix - Ref to hash of hashes distance matrix
# \param[in] $distCut          - Distance cutoff for clustering residues
# \param[in] %cluster          - Hash with keys representing current
#                                members of cluster
# \return                      - The updated cluster
#
# Recursive clustering routine. Finds the neighbours of the key residue.
# Adds them to the cluster, noting any that are new. Steps through the
# new members of the cluster and recurses to explore neighbours of these.
# Returns the updated cluster
#
# 15.04.15 Original   By: ACRM
sub DoClustering
{
    my($res, $hhDistanceMatrix, $distCut, %cluster) = @_;
    
    my @neighbours = FindNeighbours($res, $hhDistanceMatrix, $distCut);

    # Add these to the cluster noting those that are new members of 
    # the cluster
    my @newNeighbours = ();
    foreach my $neighbour (@neighbours)
    {
        if(!defined($cluster{$neighbour}))
        {
            push @newNeighbours, $neighbour;
            $cluster{$neighbour} = 1;
        }
    }

    # If there were new neighbours, recurse with those
    foreach my $neighbour (@newNeighbours)
    {
        %cluster = DoClustering($neighbour, $hhDistanceMatrix, 
                                $distCut, %cluster);
    }

    return(%cluster);
}


#*************************************************************************
#>@neighbours = FindNeighbours($res1, $hhDistanceMatrix, $distCut)
# ----------------------------------------------------------------
# \param[in] $res1             - Key residue
# \param[in] $hhDistanceMatrix - Ref to hash of hashes distance matrix
# \param[in] $distCut          - Distance cutoff for clustering
# \return                      - Array of neighbour residues
#
# Runs through the distance matrix to find residues within the 
# cutoff distance of the key residue. Will include the key residue
# itself in this list.
#
# 15.04.15 Original   By: ACRM
sub FindNeighbours
{
    my($res1, $hhDistanceMatrix, $distCut) = @_;
    my @neighbours = ();

    # Find neighbours of $res1 that are within $distCut and store their
    # labels as keys in %cluster
    foreach my $res2 (sort keys %{$$hhDistanceMatrix{$res1}})
    {
        if($$hhDistanceMatrix{$res1}{$res2} <= $distCut)
        {
            push @neighbours, $res2;
        }
    }
    return(@neighbours);
}


#*************************************************************************
#>FilterDistanceMatrix ($hhDistanceMatrix, $cutoff, %property)
# ------------------------------------------------------------
# \param[in,out] $hhDistanceMatrix - Ref to hash of hashes distance matrix
# \param[in]     $cutoff           - Property cutoff (e.g. '>50', '<20',
#                                    '=100')
# \param[in]     %property         - Hash assigning property values to
#                                    each residue
#
# Runs through the distance matrix (hash of hashes indexed by two residue 
# IDs) and retains only entries for those residues which have a property
# matching the specified cutoff. Cutoffs are specified in the form '<X',
# '>X', or '=X' - residues matching those criteria will be retained.
# If the cutoff is just given as 'X', then this is equivalent to '<X'
#
# 15.04.15 Original   By: ACRM
sub FilterDistanceMatrix
{
    my ($hhDistanceMatrix, $cutoff, %property) = @_;
    my $cmp;

    if((substr($cutoff,0,1) eq '>') || 
       (substr($cutoff,0,1) eq '<') ||
       (substr($cutoff,0,1) eq '='))
    {
        $cmp = substr($cutoff,0,1);
        $cutoff = substr($cutoff,1);
    }
    else
    {
        $cmp = '<';
    }

    # Run through the first dimension of the hash
    foreach my $res1 (sort keys %$hhDistanceMatrix)
    {
        my $match1 = CheckMatch($res1, $cmp, $cutoff, %property);

        # First dimension doesn't match property, so set all of second
        # dimension to -1
        if(!$match1)
        {
            foreach my $res2 (sort keys %{$$hhDistanceMatrix{$res1}})
            {
                delete($$hhDistanceMatrix{$res1});
            }
        }
        else
        {
            # First dimension DOES match property, so set any of second
            # dimension that don't match to -1
            foreach my $res2 (sort keys %{$$hhDistanceMatrix{$res1}})
            {
                my $match2 = CheckMatch($res2, $cmp, $cutoff, %property);
                if(!$match2)
                {
                    delete($$hhDistanceMatrix{$res1}{$res2});
                }
            }
        }
    }
}

#*************************************************************************
#>$match = CheckMatch($res, $cmp, $cutoff, %property)
# ---------------------------------------------------
# \param[in] $res       Residue identifier
# \param[in] $cmp       Comparison (>, < or =)
# \param[in] $cutoff    Cutoff value
# \param[in] %property  Hash with property values indexed by residue label
# \return               Does the property match the criteria 
#
# Check whether a residue matches the criterion for retention
#
# 15.04.15 Original   By: ACRM
sub CheckMatch
{
    my($res, $cmp, $cutoff, %property) = @_;
    my $match = 0;

    if(defined($property{$res}))
    {
        $match = 1 if(($cmp eq '<') && ($property{$res} < $cutoff));
        $match = 1 if(($cmp eq '>') && ($property{$res} > $cutoff));
        $match = 1 if(($cmp eq '=') && ($property{$res} == $cutoff));
    }

    return($match);
}


#*************************************************************************
#>%data = readTwoColumnHash($filename)
# ------------------------------------
# \param[in] $filename    File to be read
# \return                 Hash containing second column indexed by first
#
# Reads a file containing two columns into a hash
#
# 15.04.15 Original   By: ACRM
sub readTwoColumnHash
{
    my($filename) = @_;
    my %data = ();

    if(open(my $fp, $filename))
    {
        while(<$fp>)
        {
            chomp;
            s/\#.*//;             # Remove comments
            s/\s+$//;             # Remove trailing spaces
            s/^\s+//;             # Remove leading spaces
            next if(!length($_)); # Skip blank lines
            my @fields = split;
            $data{$fields[0]} = $fields[1];
        }
        close($fp);
    }
    else
    {
        $data{'ERROR'} = "Could not read file ($filename)";
    }

    return(%data);
}

#*************************************************************************
#>$distance = Distance($res1, $res2, $hhDistanceMatrix)
# -----------------------------------------------------
# \param[in] $res1             - First residue
# \param[in] $res2             - Second residue
# \param[in] $hhDistanceMatrix - Ref to hash of hashes distance matrix
# \return                      - Distance between residues (-1 on error)
# Looks up the distance between two residues in the distance hash. If
# either of the residues is not found, a value of -1 is returned.
#
# 15.04.15 Original   By: ACRM
sub Distance
{
    my($res1, $res2, $hhDistanceMatrix) = @_;
    my $retval = -1.0;
    if(defined($$hhDistanceMatrix{$res1}{$res2}))
    {
        $retval = $$hhDistanceMatrix{$res1}{$res2};
    }
    elsif($res1 eq $res2)
    {
        $retval = 0.0;
    }
    return($retval);
}

#*************************************************************************
#>PrintDistanceMatrix ($hhDistanceMatrix)
# ---------------------------------------
# \param[in]  $hhDistanceMatrix - Ref to hash of hashes distance matrix
#
# Prints the contents of the distance matrix
#
# 15.04.15 Original   By: ACRM
sub PrintDistanceMatrix
{
    my ($hhDistanceMatrix) = @_;
    foreach my $key1 (sort keys %$hhDistanceMatrix)
    {
        foreach my $key2 (sort keys %{$$hhDistanceMatrix{$key1}})
        {
            my $dist = Distance($key1, $key2, $hhDistanceMatrix);
            if($dist >= 0.0)
            {
                print "$key1 $key2 $dist\n";
            }
        }
    }
}

#*************************************************************************
#>Die($error)
# -----------
# \param[in] $error    Error message
#
# Prints an error message and exits
#
# 15.04.15 Original   By: ACRM
sub Die
{
    my($error) = @_;

    print STDERR <<__EOF;

Error (clusterResidues): $error

__EOF
    exit 1;
}

#*************************************************************************
#>ReadDistanceMatrix($filename)
# -----------------------------
# \param[in] $filename          File to be read
# \return                       Ref to hash of hashes containin distances
# 15.04.15 Original   By: ACRM
sub ReadDistanceMatrix
{
    my($filename) = @_;
    my %distMat = ();

    if(open(my $fp, $filename))
    {
        while(<$fp>)
        {
            chomp;
            s/\#.*//;             # Remove comments
            s/\s+$//;             # Remove trailing spaces
            s/^\s+//;             # Remove leading spaces
            next if(!length($_)); # Skip blank lines
            my @fields = split;
            $distMat{$fields[0]}{$fields[1]} = $fields[2];
        }
        close($fp);
    }
    else
    {
        $distMat{'ERROR'} = "Could not read file ($filename)";
    }

    return(\%distMat);
}


#*************************************************************************
#>UsageDie()
# ----------
# Prints a usage message and exits
#
# 15.04.15 Original   By: ACRM
sub UsageDie
{
    print STDERR <<__EOF;

clusterResidues V1.1 (c) 2015 UCL, Dr. Andrew C.R. Martin

Usage: clusterResidues [-d=dist][-m=min] distMatFile propFile cutoff 
                                                    [propFile cutoff [...]]

       -d=dist   Specify distance cutoff for clusters 
                 [Default: $::distCut]
       -m=min    Specify minimum number of residues in a cluster 
                 [Default: 0]
       cutoff    '<X', '>X' or '=X'

Reads a distance matrix in the form
   resid1 resid2 distance
   ...

Filters the distance matrix by retaining only residues that have 
properties matching the specified criteria. The property file is in
the form:
   resid value
   ...
e.g. a propFile could contain the solvent accessibility values for 
the residues and a cutoff of '>10' could then be used to retain 
only surface residues. Multiple propFile/cutoff pairs can be specified.

The remaining residues are clustered to find groups of residues that
are within the specified distance of each other. A residue only has
to be within the specified distance of one other residue in the cluster
to become part of the cluster.

__EOF
    exit 0;
}

