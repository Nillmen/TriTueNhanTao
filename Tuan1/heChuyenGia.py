#Kiến thức
knowledge_troi = ["nắng", "mưa", "âm u"]
knowledge_duBao = ["có mưa", "không mưa", "không biết"]
knowledge_action = ["mang ô", "không mang ô"]

knowledge_rules = [
    # Trời nắng
    {"if": {"troi": "nắng", "duBao": "có mưa"}, "then": "mang ô"},
    {"if": {"troi": "nắng", "duBao": "không mưa"}, "then": "không mang ô"},
    {"if": {"troi": "nắng", "duBao": "không biết"}, "then": "mang ô"},

    # Trời mưa
    {"if": {"troi": "mưa", "duBao": "có mưa"}, "then": "mang ô"},
    {"if": {"troi": "mưa", "duBao": "không mưa"}, "then": "mang ô"}, 
    {"if": {"troi": "mưa", "duBao": "không biết"}, "then": "mang ô"},

    # Trời âm u
    {"if": {"troi": "âm u", "duBao": "có mưa"}, "then": "mang ô"},
    {"if": {"troi": "âm u", "duBao": "không mưa"}, "then": "mang ô"},
    {"if": {"troi": "âm u", "duBao": "không biết"}, "then": "mang ô"},
]   
#Suy luận
def inference(facts):
    for rule in knowledge_rules:
        if rule["if"]["troi"] == facts["troi"] and rule["if"]["duBao"] == facts["duBao"]:
            return rule["then"]
    return "Không có hành động phù hợp!"

#Kiểm tra
def get_action(troi, duBao):
    facts = {"troi": troi, "duBao": duBao}
    action = inference(facts)
    return action

def main():
    print("***Chương trình gợi ý có nên mang ô hay không dựa trên thông tin thời tiết và dự báo***")
    troi = input("Hãy nhập thông tin về thời tiết (nắng, mưa, âm u): ")
    while troi not in knowledge_troi:
        print("Thông tin thời tiết không hợp lệ. Vui lòng nhập lại!\n")
        troi = input("Hãy nhập lại thông tin về thời tiết (nắng, mưa, âm u): ")
    duBao = input("Hãy nhập thông tin dự báo thời tiết (có mưa, không mưa, không biết): ")
    while duBao not in knowledge_duBao:
        print("Thông tin dự báo thời tiết không hợp lệ. Vui lòng nhập lại!\n")
        print(f"Hãy nhập thông tin về thời tiết (nắng, mưa, âm u): {troi}")
        duBao = input("Hãy nhập lại thông tin dự báo thời tiết (có mưa, không mưa, không biết): ")
    action = get_action(troi, duBao)
    print(f"Hành động phù hợp: {action}")

if __name__ == "__main__":
    main()