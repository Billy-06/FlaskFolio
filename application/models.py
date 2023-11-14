from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import DateTime
from datetime import datetime
from flask_login import UserMixin
from application import db
from application import app


class User(db.Model, UserMixin):
    """
    The User model. Contains the following columns:
    """
    id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username : Mapped[str] = mapped_column(String(50))
    email : Mapped[str] = mapped_column(String(50))
    password : Mapped[str] = mapped_column(String(50))
    admin_status : Mapped[bool] = mapped_column(Boolean, default=False)
    about_me : Mapped[str] = mapped_column(String(3000))
    last_seen : Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Reference: https://docs.sqlalchemy.org/en/20/orm/mapping_styles.html#mapped-class-behavior

    def __repr__(self) -> str:
        return f"User<{self.username}, {self.email}, {self.admin_status}>"
    
    def __str__(self) -> str:
        return f"Username: {self.username}\nEmail:{self.email}\nAdmin Status:{self.admin_status}>\n"

    @property
    def is_authenticated(self) -> bool:
        """
        This function checks if the user is authenticated.
        """
        return True
    
    @property
    def is_active(self) -> bool:
        """
        This function checks if the user is active.
        """
        return True
    
    @property
    def is_anonymous(self) -> bool:
        """
        This function checks if the user is anonymous.
        """
        return False
    
    def get_id(self) -> str:
        """
        This function returns the id of the user.
        """
        return str(self.id)

    def verify_password(self, password) -> bool:
        """
        This function verifies the password of a user.
        """
        return self.password == password
    

class Admin(User):
    """
    Admin model. Inherits from User. Contains the following columns:
    """
    status : Mapped[str] = mapped_column(String(10), default="admin")
    # admin_status  =db.Column(db.Boolean, default=True)

    def __repr__(self) -> str:
        return f"User<{self.username}, {self.email}, {self.admin_status}>"
    
    def __str__(self) -> str:
        return f"Username: {self.username}\nEmail:{self.email}\nAdmin Status:{self.admin_status}>\n"

    

# Create some test data
# with app.app_context():
# db.create_all()
def create_test_data(database):
    """
    Used to create test data in the database.
    """
    # Admin
    admin = User(
        username="admin",
        email="admin@admin.mail",
        password="admin",
        admin_status=True,
        about_me="Donec blandit tortor urna, eu pellentesque urna facilisis tincidunt. Nullam pretium risus a mattis dignissim. Nunc eu nisl arcu. Integer tincidunt malesuada porta. Morbi hendrerit turpis sit amet massa posuere malesuada. Nullam egestas, leo in venenatis aliquam, tortor magna molestie nulla, sit amet sollicitudin arcu eros sit amet dui. Integer nec bibendum justo. Duis consequat, augue consequat maximus imperdiet, dui justo vestibulum enim, et feugiat nisl massa ultricies velit. Nulla iaculis felis eget laoreet efficitur."
    )

    # User1-6
    user1 = User(
        username="user1",
        email="user1@user1.mail",
        password="user1",
        admin_status=False,
        about_me="Donec blandit tortor urna, eu pellentesque urna facilisis tincidunt. Nullam pretium risus a mattis dignissim. Nunc eu nisl arcu. Integer tincidunt malesuada porta. Morbi hendrerit turpis sit amet massa posuere malesuada. Nullam egestas, leo in venenatis aliquam, tortor magna molestie nulla, sit amet sollicitudin arcu eros sit amet dui. Integer nec bibendum justo. Duis consequat, augue consequat maximus imperdiet, dui justo vestibulum enim, et feugiat nisl massa ultricies velit. Nulla iaculis felis eget laoreet efficitur."
    )
    user2 = User(
        username="user2",
        email="user2@user2.mail",
        password="user2",
        admin_status=False,
        about_me="Donec blandit tortor urna, eu pellentesque urna facilisis tincidunt. Nullam pretium risus a mattis dignissim. Nunc eu nisl arcu. Integer tincidunt malesuada porta. Morbi hendrerit turpis sit amet massa posuere malesuada. Nullam egestas, leo in venenatis aliquam, tortor magna molestie nulla, sit amet sollicitudin arcu eros sit amet dui. Integer nec bibendum justo. Duis consequat, augue consequat maximus imperdiet, dui justo vestibulum enim, et feugiat nisl massa ultricies velit. Nulla iaculis felis eget laoreet efficitur."
    )
    user3 = User(
        username="user3",
        email="user3@user3.mail",
        password="user3",
        admin_status=False,
        about_me="Donec blandit tortor urna, eu pellentesque urna facilisis tincidunt. Nullam pretium risus a mattis dignissim. Nunc eu nisl arcu. Integer tincidunt malesuada porta. Morbi hendrerit turpis sit amet massa posuere malesuada. Nullam egestas, leo in venenatis aliquam, tortor magna molestie nulla, sit amet sollicitudin arcu eros sit amet dui. Integer nec bibendum justo. Duis consequat, augue consequat maximus imperdiet, dui justo vestibulum enim, et feugiat nisl massa ultricies velit. Nulla iaculis felis eget laoreet efficitur."
    )
    user4 = User(
        username="user4",
        email="user4@user4.mail",
        password="user4",
        admin_status=False,
        about_me="Donec blandit tortor urna, eu pellentesque urna facilisis tincidunt. Nullam pretium risus a mattis dignissim. Nunc eu nisl arcu. Integer tincidunt malesuada porta. Morbi hendrerit turpis sit amet massa posuere malesuada. Nullam egestas, leo in venenatis aliquam, tortor magna molestie nulla, sit amet sollicitudin arcu eros sit amet dui. Integer nec bibendum justo. Duis consequat, augue consequat maximus imperdiet, dui justo vestibulum enim, et feugiat nisl massa ultricies velit. Nulla iaculis felis eget laoreet efficitur."
    )
    user5 = User(
        username="user5",
        email="user5@user5.mail",
        password="user5",
        admin_status=False,
        about_me="Donec blandit tortor urna, eu pellentesque urna facilisis tincidunt. Nullam pretium risus a mattis dignissim. Nunc eu nisl arcu. Integer tincidunt malesuada porta. Morbi hendrerit turpis sit amet massa posuere malesuada. Nullam egestas, leo in venenatis aliquam, tortor magna molestie nulla, sit amet sollicitudin arcu eros sit amet dui. Integer nec bibendum justo. Duis consequat, augue consequat maximus imperdiet, dui justo vestibulum enim, et feugiat nisl massa ultricies velit. Nulla iaculis felis eget laoreet efficitur."
    )
    user6 = User(
        username="user6",
        email="user6@user6.mail",
        password="user6",
        admin_status=False,
        about_me="Donec blandit tortor urna, eu pellentesque urna facilisis tincidunt. Nullam pretium risus a mattis dignissim. Nunc eu nisl arcu. Integer tincidunt malesuada porta. Morbi hendrerit turpis sit amet massa posuere malesuada. Nullam egestas, leo in venenatis aliquam, tortor magna molestie nulla, sit amet sollicitudin arcu eros sit amet dui. Integer nec bibendum justo. Duis consequat, augue consequat maximus imperdiet, dui justo vestibulum enim, et feugiat nisl massa ultricies velit. Nulla iaculis felis eget laoreet efficitur."
    )

    # Get existing users
    existing_users = User.query.all()
    # Reference: 
    existing_user_emails = [user.email for user in existing_users]

    # Add only non-existing users
    if admin not in existing_users and admin.email not in existing_user_emails:
        database.session.add(admin)
    if user1 not in existing_users and user1.email not in existing_user_emails:
        database.session.add(user1)
    if user2 not in existing_users and user2.email not in existing_user_emails:
        database.session.add(user2)
    if user3 not in existing_users and user3.email not in existing_user_emails:
        database.session.add(user3)
    if user4 not in existing_users and user4.email not in existing_user_emails:
        database.session.add(user4)
    if user5 not in existing_users and user5.email not in existing_user_emails:
        database.session.add(user5)
    if user6 not in existing_users and user6.email not in existing_user_emails:
        database.session.add(user6)

    # database.session.add(admin)
    # database.session.add(user1)
    # database.session.add(user2)
    # database.session.add(user3)
    # database.session.add(user4)
    # database.session.add(user5)
    # database.session.add(user6)
    # Commit the changes
    database.session.commit()


