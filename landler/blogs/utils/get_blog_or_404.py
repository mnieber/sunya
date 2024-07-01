def get_blog_or_404(blog_id):
    return get_object_or_404(Blog, pk=blog_id)
