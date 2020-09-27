with open('students.csv', 'r') as inf:
    with open('blog/fixtures/students.json', 'w') as outf:
        outf.writelines('[\n')
        for line in inf.readlines()[1:]:
            # 62114440011	กนกพร ถึงเสียบญวน	kanokporn.th.62@ubu.ac.th	บัวบาน
            a = line.strip().split('\t')
            sid, name, email, nick = a[0], a[1], a[2], a[3]
            pythonanywhere, github = '', ''
            if len(a) > 4:
                pythonanywhere = a[4]
                if len(a) > 5:
                    github = a[5]

            outf.writelines(f"""{{
                "model": "blog.Student",
                "pk": {sid},
                "fields": {{
                    "name": "{name}",
                    "email": "{email}",
                    "nick": "{nick}",
                    "pythonanywhere": "{pythonanywhere}",
                    "github": "{github}"
                }}
            }},\n""")
        outf.writelines(']')

