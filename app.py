import os
import shutil

print(
    "\n"
    + "===" * 30
    + "\n                Simple android contact adder. Press enter to quit script.\n"
    + "===" * 30
    + "\n"
)

print("type 'backup' to backup contacts.vcf")


def add_contact():
    while True:
        new_contact_num = str(input("Enter phone number: "))
        if new_contact_num.lower() == "backup":
            backup()
        else:
            break
        if len(new_contact_num) != 10:
            print("Phone number not 10 digits")
            continue
        new_contact_fn = input("Enter first name: ")
        if new_contact_num.lower() == "backup":
            backup()
        else:
            break
        new_contact_ln = input("Enter first name: ")
        if new_contact_num.lower() == "backup":
            backup()
        else:
            break

        # Formatting phone number to add '_'
        temp = "-".join(
            new_contact_num[i : i + 3] for i in range(0, len(new_contact_num) - 3, 3)
        )
        new_num = temp + new_contact_num[-1]

        data = f"""
BEGIN:VCARD
VERSION:2.1
N:{new_contact_ln};{new_contact_fn};;;
FN:{new_contact_fn} {new_contact_ln}
TEL;CELL:{new_num}
END:VCARD
    """

        try:
            with open("contacts.vcf", "a+") as f:
                f.write(data)
            print("Added contact.")
        except:
            print("Couldn't add contact.")
            break


def backup():
    # Backup contacts.vcf
    if os.path.exists("contacts.vcf"):
        # get the path to the file in the current directory
        src = os.path.realpath("contacts.vcf")

        # seperate the path from the filter
        head, tail = os.path.split(src)
        print("path:" + head)
        print("file:" + tail)

        # let's make a backup copy by appending "bak" to the name
        dst = src + ".bak"
        # now use the shell to make a copy of the file
        shutil.copy(src, dst)

        # copy over the permissions,modification
        shutil.copystat(src, dst)
        print("backed up files to", head)
        add_contact()


if __name__ == "__main__":
    while True:
        add_contact()
