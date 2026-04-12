from lint import Lint

python_linter = Lint()
js_linter = Lint()
print(python_linter.linter(text="""print("hello world")"""))
print(python_linter.linter(text="""print("hello world")]"""))
print(js_linter.linter("""console.log("hello world");"""))
print(js_linter.linter("""console.log(data.object[1]);"""))
print(js_linter.linter("""console.log(data.object[1)];"""))