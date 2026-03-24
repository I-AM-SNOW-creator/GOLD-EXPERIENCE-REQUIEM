from ger_core import GER

# 🧪 Define what "truth" means
def validator(output):
    # Example rule: output must contain the word "optimized"
    return "optimized" in output.lower()

# 🔁 Define how to improve output
def improver(output):
    return output + " -> optimized"

# 🚀 Run GER
ger = GER(validator, improver)

result = ger.run("Create a strategy")

print("\nFinal Output:")
print(result)
