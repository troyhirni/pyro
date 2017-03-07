# pyro v0.0.2
Python Programming Library

    
    Copyright 2015-2017 Troy Hirni
    This file is part of the pyro project, distributed under
    the terms of the GNU Affero General Public License.
    
    The pyro project is free software. You can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.
    
    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    


## about pyrox

The pyro project is a python programming library built on a significant 
reorganization of code from the [aimy](http://aimy.sourceforge.net/) 
project, previously developed on sourceforge.net. The plan is to reorganize 
and optimize [the aimy project code](https://sourceforge.net/projects/aimy/), 
allowing (the code, as presented in pyro) to be potentially useful as the 
base for _any_ long-running, self-analyzing software - but specifically, 
for the next version of aimy. That is to say, once pyro reaches a sufficient 
level of stability and usability, the aimy project development will continue 
here on github in a separate project based on pyro. The development of pyro 
will also continue separately. Any updates to pyro will (sooner or later) 
be reflected in aimy, and any needs discovered in the development of aimy 
will help determine the course of pyro's development.



## update

This version adopts the great improvements from pyrox.fs; csv and tfile
objects now perform much more smoothly across python 2 and 3, the file
wrappers are more consistent in calling conventions, and the directory
class Dir has added features to make opening files much easier. The
data.pdq module has regressed a bit in preparation for sharing the
param module classes between Query and other classes soon to come, but
it's still a great way to explore and manipulate file data. The format
and Base classes have remained largely the same.
