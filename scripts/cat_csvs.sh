if [$# -eq 0]
	then
    echo "Usage: $0 <input_files>" 1>&2
fi

gawk 'FNR==1 && NR!=1{next;}{print}' $1.csv
