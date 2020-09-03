#----------------------------------------------------------------------------
# Program by Cherkasov.R.
#
#
# Version   Date        Info
# 0.1       03.09.20    Copying svg-tag from SVG file to VUE file.
#----------------------------------------------------------------------------


""""Adding by full path, checking file type (in progress) """
# path = str(input())
# if path.rfind('.svg') == -1:
#     print("Wrong file, please use svg-file")


with open("input_file.svg", "r") as f:
    text = f.read()


output_file = open('output_file.vue', 'tw', encoding='utf-8')
text_start = "<template>\n"
text_end ="""</template>

<script>
export default {
  name: 'name'
}
</script>

<style scoped lang="scss"></style>"""

start = '<svg'
end = '</svg>'

output_file.write(text_start + text[text.index(start):text.index(end)+len(end)] +"\n" + text_end )

output_file.close()
print("Done")

