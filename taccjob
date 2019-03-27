#!/bin/bash
#----------------------------------------------------
# Sample Slurm job script
#   for TACC Stampede2 KNL nodes
#
#   *** Serial Job on Normal Queue ***
# 
# Last revised: 20 Oct 2017
#
# Notes:
#
#   -- Copy/edit this script as desired.  Launch by executing
#      "sbatch knl.serial.slurm" on a Stampede2 login node.
#
#   -- Serial codes run on a single node (upper case N = 1).
#        A serial code ignores the value of lower case n,
#        but slurm needs a plausible value to schedule the job.
#
#   -- For a good way to run multiple serial executables at the
#        same time, execute "module load launcher" followed
#        by "module help launcher".

#----------------------------------------------------

#SBATCH -J myjob           # Job name
#SBATCH -o myjob.o%j       # Name of stdout output file
#SBATCH -e myjob.e%j       # Name of stderr error file
#SBATCH -p gtx          # Queue (partition) name
#SBATCH -N 1               # Total # of nodes (must be 1 for serial)
#SBATCH -n 1               # Total # of mpi tasks (should be 1 for serial)
#SBATCH -t 01:30:00        # Run time (hh:mm:ss)
#SBATCH --mail-user=sohil.shrestha@mavs.uta.edu
#SBATCH --mail-type=all    # Send email at begin and end of job
#SBATCH -A DeepFuzzCPS       # Allocation name (req'd if you have more than 1)

# Other commands must follow all #SBATCH directives...

module list

module load cuda/9.0
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/apps/cuda9_0/cudnn/7.0/lib64 
cd $WORK/TestDeepFuzz #change this line  based on where you cloned the project
pwd
date

# Launch serial code...

python clgen.py  --config /work/05359/sohil777/maverick2/TestDeepFuzz/clgen/tests/data/tiny/config.pbtxt         # Do not use ibrun or any other MPI launcher
#change this as per simulink configuration file. 
scp -r /tmp/experiments $WORK # THIS IS IMPORTANT DO NOT REMOVE 
# ---------------------------------------------------


