#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    file = None


    def do_help(self, arg):
        """Help command"""
        return True


    def do_quit(self, arg):
        """Quit command to exit the code"""
        return True


    def do_exit(self, arg):
        return True


    def do_EOF(self, arg):
        """Exit command to exit the code"""
        print ("")
        self.do_exit()

    def emptyline(self, arg):
        """empty line + ENTER shouldn’t execute anything"""
        pass


    def do_create(self, arg):
         """Create instance of class"""

        args = parse(arg)
        if len(args) == 0:
            print("** class name  missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        show <class>  <id>
        Display string representation of the class instance
        """
        args = parse(arg)
        objdict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """
        destroy <class>  <id>
        delete a class instance of a given id
        """
        args = parse(arg)
        objdict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id doesn't exist **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """
        usage; all <class> or <class>.all()
        Display all instances of a given class
        """
        args = parse(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objs = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    objs.append(obj.__str__())
                elif len(args) == 0:
                    objs.append(obj.__str__())
            print(objs)

    def do_update(self, arg):
        """
        usage: update <class> <id>
        Update a class instance of a given id by adding \
            or updating a given attribute
        """
        args = parse(arg)
        objdict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        elif len(args) == 1:
            print("** instance id missing **")
            return False
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
            return False
        elif len(args) == 2:
            print("** attribute name missing **")
            return False
        elif len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        elif len(args) == 4:
            obj = objdict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = objdict["{}.{}".format(args[0], args[1])]
            for k, v in eval(args[2]).items():
                k_in_keys = k in obj.__class__.__dict__.keys()
                type_in = type(obj.__class__.__dict__[k]) in {str, int, float}
                if (k_in_keys and type_in):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
