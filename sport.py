import json
from pathlib import Path

def extract_english_messages(input_file: str, output_file: str = None):
    """
    Extract all English messages from the multilingual JSON file.
    """
    input_path = Path(input_file)
    
    if not input_path.exists():
        print(f"Error: File '{input_file}' not found.")
        return

    # Read the JSON file
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Extract English entries
    english_messages = []
    
    for item in data:
        if isinstance(item, dict) and item.get("lang") == "EN":
            english_messages.append({
                "id": item.get("id"),
                "preset_id": item.get("preset_id"),
                "category": item.get("category"),
                "text": item.get("text"),
                "msg_emoji": item.get("msg_emoji"),
                "continent": item.get("continent")
            })

    print(f"✅ Extracted {len(english_messages)} English messages.\n")

    # Print first few for preview
    for msg in english_messages[:5]:
        print(f"{msg['preset_id']:3d} | {msg['msg_emoji']} {msg['text']}")
    if len(english_messages) > 5:
        print(f"... and {len(english_messages)-5} more.")

    # Save to file if output path is provided
    if output_file:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(english_messages, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Saved English messages to: {output_file}")

    return english_messages
# ============================
# Usage Examples
# ============================

if __name__ == "__main__":
    # Example 1: Just extract and print
    messages = extract_english_messages("sport.json")

    # Example 2: Extract and save to new file
    messages = extract_english_messages("sport.json", "english_messages.json")

    # Example 3: Extract only the text strings as a simple list
    # texts_only = [msg["text"] for msg in messages]
    # print(texts_only)


