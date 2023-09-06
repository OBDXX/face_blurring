#!/bin/bash

################################################################################
# Title:       
# Description: 
# Author:      
# Date:        
# Version:     1.0
################################################################################

# Usage: 



# Description:


# Notes:

# Exit codes:
#   0   Success
#   1   General error
#   2   Invalid arguments

# Dependencies:

#--- Script starts here ---

# Pull Docker image
docker pull tensorflow/tensorflow
docker tag tensorflow/tensorflow corsound
docker build --no-cache . -t corsound

#
cd
cd corsound
#--- Script ends here ---

