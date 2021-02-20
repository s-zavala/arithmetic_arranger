def format_lines(mainDict, solution):
    """
    Args: the mainDict and a bool for solution.
    Returns a list of four lines.
    Line 1 reformats the first operand.
    Line 2 reformats the operator and the second operand.
    Line 3 adds dashes for visual ease.
    Line 4 displays the answer. Takes solution arg. Optional
    """
    align='>'
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    keys = sorted(mainDict.keys())
    for prob in keys:
        # add a string to line1
        width = mainDict[prob]['colWidth']
        line1 += '{term1:{align}{width}}'.format(term1 = mainDict[prob]['term1'], width=width, align=align)
        if prob != keys[-1]:
            line1 += ' '*4
        # Add str to line2 with second operand and operator.
        line2 += '{operator}{term2:{align}{width}}'.format(operator = mainDict[prob]['operator'], term2 = mainDict[prob]['term2'], width=width-1, align=align)
        if prob != keys[-1]:
            line2 += ' '*4
        line3 += '-'*width
        if prob != keys[-1]:
            line3 += ' '*4
        if solution == True:
            line4 += '{answer:{align}{width}}'.format(answer = mainDict[prob]['sum'], width=width, align=align)
            if prob != keys[-1]:
                line4 += ' '*4
    lines = line1 + '\n' + line2 + '\n' + line3
    if solution == True:
        lines += ('\n' + line4)
    return lines