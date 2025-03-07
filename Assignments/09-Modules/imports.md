### Importing modules
Importing modules lets us use the functions, objects, classes etc. specific to that module

For instance the datetime module:

    import datetime
    print(datetime.datetime.now()   # Will print current time
    # module = datetime, class = datetime, method = now()    

It's possible to be more specific with imports instead of importing entire modules:

    from datetime import datetime
    print(datetime.now())

Now we imported the datetime class specifically and can call upon its methods.

It's also possible to assign a name to the imported module:

    from datetime import datetime as d
    print(d.now())
