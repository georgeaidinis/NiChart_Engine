import pandas as pd
import sys

def merge_two(in_csv1, in_csv2, key_var, out_csv):
    """
    Merge two input data files
    Output data includes an inner merge
    """
    
    df1 = pd.read_csv(in_csv1)
    df2 = pd.read_csv(in_csv2)
    
    df_out = df1.merge(df2, on = key_var)

    # Write out file
    df_out.to_csv(out_csv, index=False)

if __name__ == "__main__":
  # Access arguments from command line using sys.argv
  if len(sys.argv) != 5:
      print("Error: Please provide all required arguments")
      print("Usage: python merge_two.py in_csv1.csv in_csv2.csv key_var out_csv.csv")
      sys.exit(1)

  in_csv1 = sys.argv[1]
  in_csv2 = sys.argv[2]
  key_var = sys.argv[3]
  out_csv = sys.argv[4]
  
  # Call the function
  merge_two(in_csv1, in_csv2, key_var, out_csv)

  print("Merge complete! Output file:", out_csv)
