from code.classes import smartgrid



if __name__ == "__main__":
    # Set-up parsing command line arguments
    parser = argparse.ArgumentParser(description = "adding houses to batteries")

    # Adding arguments
    #parser.add_argument("output", help = "output file (csv)")
    parser.add_argument("input_houses", help="houses file")
    parser.add_argument("input_batteries", help="batteries_file")

    # Read arguments from command line
    args = parser.parse_args()

    # Run main with provide arguments
    df_houses, df_batteries = load_df(args.input_houses, args.input_batteries)

    #my_smartgrid = Smartgrid.from_file(args.input_houses, args.input_batteries)

    my_smartgrid = smartgrid.Smartgrid(df_batteries, df_houses)
