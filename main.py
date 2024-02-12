def wc(content : str) -> int:
    return len(content.split())

def occurence_map(content : str) -> dict[str : int]:
    occ_map = {}
    for word in content.split():
        for c in word.lower():
            if not c.isalpha():
                continue
            if c in occ_map:
                occ_map[c] += 1
                continue
            occ_map[c] = 1
    return occ_map

def sort_on(report_list_element : dict) -> str:
    return report_list_element["count"]

def get_report(occ_map : dict) -> list[str]:
    report_list = []
    for key in occ_map:
        report_list.append({"letter": key, "count": occ_map[key]})
    report_list.sort(reverse=True, key=sort_on)
    return report_list

def main():
    print("--- Begin report of books/frankenstein.txt ---")
    with open('books/frankenstein.txt', 'r') as f:
        content = f.read()
        print(f"{wc(content=content)} words found in the document")
        print()
        report_list = get_report(occurence_map(content=content))
        for r in report_list:
            print(r)
    return

if __name__ == '__main__':
    main()