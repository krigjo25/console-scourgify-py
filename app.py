#   Scourgify
#   Author :    krigjo25

#   Importing Python responsories
import sys, csv

def main():

    
    try: 
        #   Ensure the user provides two command-line arguments
        if len(sys.argv) != 3: 
            raise SystemError("Invalid number of arguments")

        #   Ensure the first argument is a CSV file
        if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]: 
            raise SystemError(".csv file was not foundNot a CSV file")

    except SystemError as e:
        print(f"System Error : {e}\nUsage : python scourgify.py  [path/to/file.csv] [path/to/outputfile.csv]\n The system exits with code 1")
        sys.exit(1)

    CSVReader(sys.argv[1], sys.argv[2])

def CSVReader(Infile, Outfile):

    """
        #   Author :    krigjo25
        #   Read the CSV file and write to a new CSV file
        #   Time complexity : O(1000) = 0.005s
    """

    #   Initializing a list
    student = []
    fieldnames = ["first name", "last name", "house"]

    #   Open the csv file & write to a new CSV file
    with open(f"{Infile}", 'r') as f:

        #   Parse the CSV file
        for row in csv.DictReader(f):

            last, first = row["name"].split(",")
            student.append(
                {
                    "first name": first, 
                    "last name": last, 
                    "house": row["house"]
                })

    with open(f"{Outfile}", 'w') as w:
        
        #   Initialize the csv writer
        cw = csv.DictWriter(w, fieldnames=fieldnames)

        #   Write the rows
        cw.writeheader()
        cw.writerows(student)

if __name__ == '__main__':
    main()
