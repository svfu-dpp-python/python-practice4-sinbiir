import os





def find_maximums(path):
    arrow = []
    with open(f"{path}", "r") as f:
    
        for i in f.readlines():
            arrow.append(max(map(int,input().split(" "))))
        
    return arrow

def write_range(name, a, b):
    with open(f"{name}", "w") as f:
        for i in range(a,b):
            f.write(str(i))



def count_files(directory_path):
    files_list = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    return len(files_list)

def open_in_notepad(filename):
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден.")
        return
    os.system(f"notepad++ {filename}")

if __name__ == "__main__":
    # ваш тестовый код

    open_in_notepad("example.txt")