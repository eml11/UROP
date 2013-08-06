#!/bin/bash
# This script runs a "performance" job using fluidity-cx1 modules, 
#  the PYTHONPATH and FLUIDITY_BIN variables point to the relevant
#  bzr branch, and option -v1 is used for fluidity verbosity.
# Job name : 
#PBS -N WWbcP1P1
# Time required in hh:mm:ss :
#PBS -l walltime=72:00:00
# Resource requirements :
#PBS -l select=1:ncpus=8:mem=600mb
# Files to contain standard output and standard error :
# Queue specification :
##PBS -q pqese

PROJECT=sphericalShell.flml
echo Working directory is $PBS_O_WORKDIR 
cd $PBS_O_WORKDIR
rm -f stdout* stderr* core* *.pyc

. /etc/profile.d/module.sh

module load intel-suite/11.1
module load mpi
module load vtk/5.8.0
module load netcdf
module load udunits
module load parmetis
module load petsc/3.1-p8-intel-11
module load zoltan
module load libscotch

export FLUIDITY=/work/avdis01/fluidity/trunk_performance
export FLUIDITY_BIN=$FLUIDITY/bin
export PYTHONPATH=$PYTHONPATH:$FLUIDITY/python/:$FLUIDITY/scripts/

pbsdsh2 cp -rf $PBS_O_WORKDIR/\* $TMPDIR/
echo $TMPDIR > where_am_i
cd $TMPDIR
pbsexec -grace 55 mpiexec $FLUIDITY_BIN/fluidity -v1 -l $PROJECT
pbsdsh2 cp -rf $TMPDIR/\* $PBS_O_WORKDIR
