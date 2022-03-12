# echo assigning variables
echo "Assigning variables"
script=$1
input_text_file=$2
echo script: $script
echo input_text_file: $input_text_file

# echo to the console that the program is running
echo -e "\nRunning the program ${script}"


if [ $# -eq 3 ]; then
    output_text_file=$3
fi

#if the python script is available and then if the input text file is available and if there is a third command line argument then run the python script
if [ -f $script ] && [ -f $input_text_file ] && [ $# -eq 3 ]; then
    python $script $input_text_file > $output_text_file
    echo -e "\nProgram has finished running and is returned in the output text file ${output_text_file}."
#if the python script is available and the text file is available but output_text file is not defined, then run the python script
elif [ -f $script ] && [ -f $input_text_file ] && [ $# -eq 2 ]; then
    python $script $input_text_file
    echo -e "\nProgram has finished running."
#if none of the files are available then return an error message indicating which files were missing
else
    echo "Error: Missing file(s)"
    if [ ! -f $script ]; then
        echo "Script: $script"
    fi

    if [ ! -f $input_text_file ]; then
        echo "Input text file: $input_text_file"
    fi
fi

