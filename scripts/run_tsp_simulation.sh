#!/bin/bash
export LD_LIBRARY_PATH="${1}:$LD_LIBRARY_PATH";
${2}/generate_tsp_csv ${3} ${4} ${5} ${6} ${7} ${8} ${9} ${10} ${11} ${12}
