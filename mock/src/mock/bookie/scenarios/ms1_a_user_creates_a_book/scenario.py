from sunya import (
    goal,
    add_scenario,
    get_scenario,
    the,
    G as g,
    R as r,
    I as i,
    it,
)

scenario_name = f"bookie/a_user_creates_a_book_with_lorem_ipsum"


def start():
    with add_scenario(scenario_name):
        with goal(i.create_a(r.book).with_random_lorem_ipsum_text()):
            # Run the command line tool
            with the(r.user).runs_the(g.bookie_cli).with_args(
                "create-book", "--title", "My Book", "--chapters", "3"
            ):
                # Create the book
                with the(g.bookie_cli).calls_the(g.create_book_action):
                    with it().creates_the(r.book):
                        assert r.book.title == "My Book"

                    # Create chapters
                    for chapter_idx in range(3):

                        # Create chapter
                        with (
                            it()
                            .calls_the(g.create_chapter_action)
                            .to_create_the(r.current_chapter)
                        ):
                            # For each paragraph to be created in this chapter
                            for para_idx in range(5):
                                with (
                                    it()
                                    .calls_the(g.create_paragraph_action)
                                    .to_create_a_paragraph_for_the(r.current_chapter)
                                ):
                                    pass

                            assert len(r.current_chapter.paragraphs) == 5

                    # Finally, the CLI outputs the information about what was created
                    with the(g.bookie_cli).outputs_book_creation_summary(r.book):
                        pass

    return get_scenario(scenario_name)


def run():
    return start()


if __name__ == "__main__":
    run()
