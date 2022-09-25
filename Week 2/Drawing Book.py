# Given a book where page 1 is always the front of the right page and where the last page can only
# be numbered on its front, generate the minimum number of pages needed to be flipped to reach page
# p given a book of page length n.  Note that the flip to open the book does not count.

# Solution: we use control flow to first catch the exception case, which is a book of length 1.  Such
#           a book always requires 0 flips, since the opening of the book reaches the page.  Next, for
#           page numbers that are less than halfway through the book, we cover 2 pages with every flip.
#           The same goes for pages that are greater than half (we flip starting from the back of the
#           book in these cases).  However, note that because the last right page can only be printed on
#           the front and the front of the right page must be an odd number, even-length books require an
#           extra flip if the desired page number is n - p, whereas odd-numbered books do not.
#           Time complexity: O(N)

def pageCount(n, p):
    # Write your code here
    if n < 2:
        return 0
    elif p <= n / 2:
        return int(p / 2)
    elif p > n / 2:
        if n % 2 == 0 and p == n - 1:
            return 1
        else:
            return int((n - p) / 2)


