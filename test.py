from app import db, Computer

db.create_all()

dell_ins = Computer('Dell Inspiron 5559', 1024)
apple_mac = Computer('MacBook Pro', 2048)
lenovo_p = Computer('Lenovo Legion', 5034)

# db.session.add(dell_ins)
# db.session.add(apple_mac)
# db.session.add(lenovo_p)
# db.session.commit()

# print(dell_ins.id)
# print(lenovo_p.id)
# found = Computer.query.filter_by(name="Lenovo Legion").first()
# db.session.delete(found)
# print(Computer.query.all())
print(User.)