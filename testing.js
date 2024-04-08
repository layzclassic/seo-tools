    <!-- Include Brython library directly within the body -->
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/brython@3.9.5/brython.min.js"></script>

    <script type="text/python">
        from browser import document

        def greet(event):
            name = document['name_input'].value
            document['output'].text = f"Hello, {name}!"

        document['greet_button'].bind('click', greet)
    </script>

    <script type="text/javascript">
        // Initialize Brython
        brython();
    </script>
