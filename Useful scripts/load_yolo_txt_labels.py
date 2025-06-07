def load_yolo_labels(label_dir, file_names):
    labels = {}
    for name in file_names:
        txt_name = os.path.splitext(name)[0] + ".txt"
        txt_path = os.path.join(label_dir, txt_name)
        if os.path.exists(txt_path):
            with open(txt_path, 'r') as f:
                line = f.readline()
                if line.strip():
                    labels[name] = int(line.split()[0])
                else:
                    labels[name] = 0
        else:
            labels[name] = 0
    return labels