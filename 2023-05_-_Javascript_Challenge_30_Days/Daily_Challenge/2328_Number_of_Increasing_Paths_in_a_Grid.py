class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        '''
        Naive solution

        A line can only start in a square when there is no lower square next to it
        that is, if there is a lower square next to it, any line starting here would have been longer
        starting from there: To find the longest line, this is important.

        Since we also want to count the smallest lines, let's discuss them separately.

        Each square is a path of length 1, so we can just add n*m as a constant factor.

        OR
        we do breath-first-search and count the individual starts, no difference

        HOWEVER when counting a path of length two that ends in the beginning of another path
        will lead to a lot of re-visiting of known paths and squares, so we've got to be 
        a little bit smarter about this.

        One idea is to find all paths of two
        and those that overlap for paths of three
        and since we are increasing strictly we don't have to worry about loops

        Outline for an algorithm:
        a) Constanct factor m x n for all 1 length paths
        b) Find all neighbors that are higher: Give us paths of length 2
        c) Store start and end in a list "paths2"
        d) If an end_i matches a start_j insert into "paths3" the (start_i, end_j) tuple
        e) This can go iteratively until no extension of the existing paths can be found.
          
        This algorithm certainly can be optimized, but we'll worry about this
        '''
