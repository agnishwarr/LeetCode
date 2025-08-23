from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        Justify a list of words so each line has exactly maxWidth characters.
        Rules
          1. Greedily pack as many words per line as fit
          2. For non final lines distribute spaces as evenly as possible
             extra spaces go to earlier gaps from the left
          3. Final line is left aligned, single spaces between words, pad trailing spaces
        """
        res = []                                  # final list of justified lines
        i = 0                                      # index of the current word

        # Process words until all are placed into lines
        while i < len(words):
            line_len = 0                           # total length of words in the current line, no spaces yet
            j = i                                  # j will move to the first word that does NOT fit

            # Try to add as many words as possible to this line
            # The line consumes lengths of words plus one space between words except before the first word
            while j < len(words):
                word_len = len(words[j])           # length of the candidate word
                # If we add words from i..j, there will be (j - i) gaps between them
                # Current total footprint if we include words[j] equals
                #   current line_len of words plus word_len plus number of gaps which equals (j - i)
                if line_len + word_len + (j - i) <= maxWidth:
                    line_len += word_len           # accept this word, update raw letters length
                    j += 1                         # try next word
                else:
                    break                          # cannot add more words to this line

            # Now words[i..j-1] are in this line
            num_words = j - i                      # how many words we packed into this line
            is_last_line = j == len(words)         # check if this is the last line of the paragraph

            # Build the line according to justification rules
            if num_words == 1 or is_last_line:
                # Left justify
                # Join words with a single space, then pad the right with spaces to maxWidth
                line = " ".join(words[i:j])        # single spaces between words
                spaces_to_add = maxWidth - len(line)  # remaining spaces for right padding
                line = line + " " * spaces_to_add  # pad to exact width
            else:
                # Full justify for middle lines with at least two words
                total_spaces = maxWidth - line_len     # total spaces to distribute across gaps
                gaps = num_words - 1                   # number of gaps between words
                base_space = total_spaces // gaps      # minimum spaces per gap
                extra = total_spaces % gaps            # first extra gaps get one additional space

                parts = []                             # accumulate word plus its following spaces
                for k in range(i, j):
                    parts.append(words[k])             # add the word
                    if k < j - 1:                      # if not the last word of the line
                        # compute spaces for this gap
                        # first `extra` gaps get one more space
                        spaces_here = base_space + (1 if (k - i) < extra else 0)
                        parts.append(" " * spaces_here)  # append that many spaces
                line = "".join(parts)                  # merge into a single justified line

            res.append(line)                           # collect the constructed line
            i = j                                      # advance to the next line starting word

        return res