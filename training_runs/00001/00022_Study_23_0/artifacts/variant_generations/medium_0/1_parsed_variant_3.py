def sat(answer):
    return all(answer[i] == 'dee'[i] for i in range(len(answer)))

if __name__ == "__main__":
    print("Parsed sat() loaded successfully")
