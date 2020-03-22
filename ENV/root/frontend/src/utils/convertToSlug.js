
{/*
    Purpose: Script converts the passed in text into a "SLUG" value.

    Date created: 2/19/2020
 */}

export function convertToSlug(Text)
{
    return Text
        .toLowerCase()
        .replace(/[^\w ]+/g,'')
        .replace(/ +/g,'-');
}