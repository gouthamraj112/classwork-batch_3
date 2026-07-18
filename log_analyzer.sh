count_errors(){
echo "number of error messages: "
grep -c "ERROR" server.log
}

#function to display warning messages
show_warning(){
echo "warning messages: "
grep "WARNING" server.log
}

#function to replace the error with CRITICAL
replace_error(){
echo "Replacing ERROR with CRITICAL...."
sed 's/ERROR/CRITICAL/g' server.log
}

echo "================================"
echo "      Log File Analyzer         "
echo "================================"

count_errors
echo
show_warning
echo
replace_error

