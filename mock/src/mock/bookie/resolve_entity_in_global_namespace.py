import mock.bookie.namespace as B


def resolve_entity_in_global_namespace(name):
    if name == "create_book_action":
        return B.Books.Actions.CreateBook()
    if name == "create_chapter_action":
        return B.Chapters.Actions.CreateChapter()
    if name == "create_paragraph_action":
        return B.Chapters.Actions.CreateParagraph()
    if name == "bookie_cli":
        return object()  # Placeholder implementation

    return None
