# Syd - Synamic Data Format: Better alternative to yaml, toml, json, and many others.
A new data format that was invented out of frustration in existing data formats like yaml, toml, json, etc.
It was created and improved bit by bit during the development of two years old framework Synamic.

The features, flexibility, extensibility, and intuitiveness that were not found in those formats was the motivation behind this.
The work begun in 2017 inside the framework Synamic and now it is being released as a separate library.

# Draft & Old Doc from Comments (Not Updated as the Code)
`# lots of thoughts needed.`

-------------------------------------------------------------------------
## comments

`//` is a single line comment.

`#` is also a single line comment.

**Where comments can appear:**
1. Inside a block: on an independent line that does not contain scalar data
2. Inside a block list: on an independent line that does not contain scalar data
3. After the starting curly brace/bracket of block/list.
4. On an empty line outside of blocks/block lists. That is on the independent lines of file. Be noted that, a file is considered block and it
    Contains key value pairs.

Where it cannot appear:
Within or at the end of scalar data: string, number, date
Within or at the end of linear list: (a, t, 5)

Comments may be preceded by spaces and/or tabs.

`\#` is a literal hash. Hash inside strings are also literal hash.

`\//` is also literal two forward slash.


## import/include
Other data files can also be imported/included with !include <relative file name with or without ext>

!include must be on it's own line.

## load model

Models can be specified by the system


## interpolation

Interpolation happens in the second pass. So, after everything is loaded, the non-recursive keys can be found
easily.

`{{ key }}`

`{{ key.subkey }}`

key can be found in the current data file or from an included file.

To put literal `{{` then just precede it with a single backward slash. `\{{`
This is not needed for single curly brace.

## escaping

Escaping is done through backward slash. Escaping are relaxed and special in synamic data file.
To escape a backward slash escape it with another one.
Escaping does not take place in each and every thing.

CALCEL, don't want to keep type hinting, need to make things clean for end user | data __document_types

## Data type enforcement

If you want to force type on a data then you can use the following key suffixes.
```
!n -> number
!i -> integer
!f -> float
!d -> date
!t -> time
!dt -> date-time
!s -> string
!l -> list
!b -> boolean
```
**Other suffixes can also be defined by the system with models**

1) Number: Priority Top (1)
```
-> 1 <- is a number.
-> 2.5 <- is a number.
```
**1 & 1.0 are equal.**

2) Date, Time & Datetime: Priority 2

If something falls in the format of date, time or datetime that is considered is date.
The default formats are.

If you want a date like format to be treated like string then use quoted string.

Date: <4 digit year>:<1 or 2 digit month within the range of 1-12>:<1 or 2 digit date within the range defined by month>
Time: <1 or 2 digit hour within range of 0-23 or 0-12 if AM/PM present>:<1 or 2 digit minute 1-59>:<Optional: 1 or 2 digit seconds>:<Optional: AM/PM - case insensitive>
Datetime: Combination of date & time separated by space character(s) - spaces/tabs.

3) String: Priority 3 

-> Strings 1 (no quotation): strings does not need any quotation mark. No special/escape characters - everything is literal char.
key: this is a string value, leading and trailing spaces are ignored.

-> String 2 (single quotation): if the value part starts with a single quotation then it is considered single
quoted string. a quotation inside it must be escaped with backward slash. 

4) List: Priority 4

*If a key ends with "!l" or "!L" then it will be considered a list. So, there is no need to to delimit
list elements with [ & ]*

- List elements are separated by commas. You cannot enforce type on list elements, they must be inferred.
- if you want special treatment then use model based parsing.

- List elements can contain numbers, single line strings, date, time, date-time, boolean data __document_types only.
- Strings must be single line strings. You can use multiline strings with triple quoting.

4) Other data: Priority 3

If a key is mentioned in an associated model then the string is parsed.

 

-------------------------------------------------------------------------


!include values-dev.txt
!include_if_exists values-super-dev2.txt

key1 : value
// data type specification cancelled: key10 !s the colon after the key is optional.
// data type specification cancelled: key11 !l : this is, a typed, key, with type list
key2 {
        multilevel: value 2
}

## multiline text:
 key must be suffixed with ~, in this case there must not be any type specifier.
**as described above, the colon is optional. But a multiline text must be enclosed in curly braces.**

```
key3~: {

}
```

*if the there is no text after { then this empty line is not included in the output.*
*if it contains some text then the preceding spaces are also considered to be included in the calculation of indentaion.*

```
key30~ {
         Indentation does not start here.
  Indentation starts here.
  Tab normalization happens (no replace - just counted virtually) for counting indentation. One tab is considered
     as 4 spaces.
}
```

*if you do not want any indentation detection happen and take all the text literally, then you must use double tilde.*

```
key31~~ : {
   All preceded spaces are kept
Intact, no matter at how many level the key is nested.
}
```

## Nested values
```
key4: {  
    k1: {
         k11: value
    }
    k2: single line
    multiline~ {
    }
}
```