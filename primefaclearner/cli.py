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
        help="Lower limit of the numbers you'll be quizzed about."
    )
    quizme_parser.add_argument(
        "num2", type=int,
        help="Upper limit of the numbers you'll be quizzed about."
    )

    # Subcommand for 'quizme-reverse'
    quizme_reverse_parser = subparsers.add_parser('quizme-reverse', help='Quizes you about the number corresponding to a prime factorization in a given range.')
    quizme_reverse_parser.add_argument(
        "num1", type=int,
        help="Lower limit of the numbers you'll be quizzed about."
    )
    quizme_reverse_parser.add_argument(
        "num2", type=int,
        help="Upper limit of the numbers you'll be quizzed about."
    )

    # Subcommand for 'showpf'
    showpf_parser = subparsers.add_parser('showpf', help='Shows the prime factorization of a given number or multiple numbers in a given range.')
    showpf_parser.add_argument(
        "num", type=int,
        help="Number to factorize or lower limit of the numbers to factorize."
    )
    showpf_parser.add_argument(
        "num2", type=int, nargs='?', default=None,
        help="Upper limit of the numbers to factorize. Only needed when you want to obtain the prime factorization of more than one number."
    )

    # Define completions for each subcommand
    completions = {
        'quizme': [],
        'quizme-reverse': [],
        'showpf': []
    }

    argcomplete.autocomplete(parser, always_complete_options=False, **completions)  # Enable tab completion
    args = parser.parse_args()

    if args.subcommand == 'quizme':
        quizme(args.num1, args.num2)
    elif args.subcommand == 'quizme-reverse':
        quizmereverse(args.num1, args.num2)
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

