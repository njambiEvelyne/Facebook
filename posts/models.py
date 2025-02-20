from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Posts(models.Model):
    content = models.CharField(max_length=300, null=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return f"Post by: {self.posted_by.username}"


class Comment(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )  # Tracks who commented
    content = models.TextField()

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.id}"


class ProfilePicture(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, related_name="profile_picture"
    )
    image_url = models.URLField(blank=True)  # Allow blank values

    def __str__(self):
        return (
            f"Profile Picture of {self.user.username if self.user else 'Deleted User'}"
        )


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    members = models.ManyToManyField(
        User, related_name="user_groups"
    )  # Avoid conflict!
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
