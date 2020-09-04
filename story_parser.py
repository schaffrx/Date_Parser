import re

class Story_Parser:

    def __init__(self, target_file: str):
        self.target_file = target_file
        with open(self.target_file, 'r') as file:
            self.content = file.read()

    def get_stories(self)-> list:
        """Uses regular expressions to separate content via tabs and newline
        Returns
        -------
        list
            a list of all content matching regex pattern
        """
        pattern = re.compile("[^\t\n]+")
        stories:list = pattern.findall(self.content)
        return (stories)

    def remove_targets(self, target_list: list, content_list: list) -> list:
        """Uses list comprehensions to remove target list from content list

        Parameters
        ----------
        target_list : list
            The items you want removed from the content list
        content_list : list
            The original list to remove content from 

        Returns
        -------
        list
            a list without the target_list items
        """
        trimmed_content = [x for x in content_list if x not in target_list]
        return(trimmed_content)
        
    def require_num_words(self, num_chars: int, content_list: list) -> list:
        """Utility method that removes index entries under the min length

        Parameters
        ----------
        num_chars : int
            The minimum threshold of characters to be included in the list
        content_list : list
            The input list to be targeted

        Returns
        -------
        list
            a list containing content of the minimum threshold
        """
        trimmed_content: list = []
        for content in content_list:
            if (len(content)) >= num_chars:
                trimmed_content.append(content)
        return(trimmed_content)


if __name__ == '__main__':
    new_story = Story_Parser('missoula.txt')
    split_story = new_story.get_stories()
    print(split_story)