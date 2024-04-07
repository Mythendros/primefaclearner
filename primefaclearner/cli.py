import argparse
import argcomplete
from .primefaclearner import quizme
from .primefaclearner import showpf
from .primefaclearner import quizmereverse

def main():
    parser = argparse.ArgumentParser(
        description="A Cli-Tool to help you memorize prime factorizations!"
    )
    subparsers = parser.add_subparsers(title='subcommands', dest='subcommand')

    # Subcommand for 'quizme'
    quizme_parser = subparsers.add_parser('quizme', help='Quizes you about the prime factorization of numbers in a given range.')
    quizme_parser.add_argument(
        "num1", type=int,
        help="Lower limit of the numbers you'll be quized about."
    )
    quizme_parser.add_argument(
        "num2", type=int,
        help="Upper limit of the numbers you'll be quized about."
    )

    # Subcommand for 'showpf'
    showpf_parser = subparsers.add_parser('showpf', help='Shows the prime factorization of a given number or multiple numbers in a given range.')
    showpf_parser.add_argument(
        "num", type=int,
        help="Number to factorize or lower limit of the numbers to factorize."
    )
    showpf_parser.add_argument(
        "num2", type=int, nargs='?', default=None,
        help="Upper limit of the numbers to factorise. Only needed when you want to obtain the prime factorization of more than one number."
    )

    argcomplete.autocomplete(parser)  # Enable tab completion
    args = parser.parse_args()

    if args.subcommand == 'quizme':
        quizme(args.num1, args.num2)
    elif args.subcommand == 'showpf':
        if args.num2 is None:
            showpf(args.num)
        else:
            showpf(args.num, args.num2)
    else:
        print("primefaclearner")
        print("Version: 0.0.1")
        print("Type 'primefaclearner -h' for help")
       

if __name__ == "__main__":
    main()


