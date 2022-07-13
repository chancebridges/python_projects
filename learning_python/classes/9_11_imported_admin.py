from user_privileges_admin import User, Privelage, Admin

admin_1 = Admin("Chance", "Bridges", "24", "male", "5'7", "priv")
Admin.greet_user(admin_1)
admin_1.privelages.show_privelages()