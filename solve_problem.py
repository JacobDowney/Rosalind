import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="Move file & run problem")

    parser.add_argument('prob', help='The problem folder', type=str)
    args = parser.parse_args()

    type = 'Bioinformatics_Stronghold'

    txt_file = f'rosalind_{args.prob.lower()}.txt'
    path_to_txt = f'~/Downloads/{txt_file}'
    path_to_prob = f'~/CS_Projects/Rosalind/{type}/{args.prob.upper()}/'
    move_command = f'mv {path_to_txt} {path_to_prob}'
    os.system(move_command)

    run_command = f'python {path_to_prob}solution.py {path_to_prob}{txt_file}'
    os.system(run_command)

if __name__ == '__main__':
    main()
else:
    print("NOT COMPATIBLE")
