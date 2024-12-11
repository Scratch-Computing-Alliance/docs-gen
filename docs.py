generated_docs = []

print("we are gonna generate some docs starters in markdown.")
print("know that some of this will have to be changed later.")

generated_docs.append("# docs")
generated_docs.append("## about")
about = input("info about your project: ")
generated_docs.append(about)
generated_docs.append("## copyright")
copyright = input("copyright info. whats the license for your project? is there any copyright info?")
generated_docs.append(copyright)
generated_docs.append("## dependencies")
generated_docs.append("list dependencies for your project")
generated_docs.append("## install")
generated_docs.append("how to install your project this may eb multiple lines and you can use '+' in markdown to add steps")

with open("generated_docs.md", "w") as file:
    for item in generated_docs:
        file.write(f"{item}\n")

print("finished!")
