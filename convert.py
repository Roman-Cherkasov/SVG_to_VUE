#----------------------------------------------------------------------------
# Program by Cherkasov.R.
#
#
# Version   Date        Info
# 0.2       05.09.20    Copying svg-tag from SVG file to VUE file.
#                       Added the ability to convert multiple files, stop the program if there are no files to convert.
#----------------------------------------------------------------------------

import os
import shutil

input_folder = "input_files"
output_folder = "result_files"

def collect_files(folder_name):
      files = os.listdir(folder_name)
      svg_counter = 0
      files_list = []
      for i in files:
            if i.endswith(".svg"):
                  svg_counter +=1
                  files_list.append(i)          
      if svg_counter == 1:
            print("There is " + str(svg_counter) +" svg file.\n")
      elif svg_counter > 1:
            print("There are " + str(svg_counter) +" svg files.\n")
      else:
            print("There are no svg files. Please add them and try again.")
            raise SystemExit(1)
      return files_list

def convert(file_name):
      start = '<svg'
      end = '</svg>'
      text_start = "<template>\n"
      text_end ="""</template>
      <script>
      export default {
        name: 'name'
      }
      </script>
      <style scoped lang="scss"></style>"""

      with open(file_name, "r") as file:
            text = file.read()
      result_file = file_name[:-4] + '.vue'
      output_file = open(result_file, 'tw', encoding='utf-8')
      output_file.write(text_start + text[text.index(start):text.index(end)+len(end)] +"\n" + text_end )
      output_file.close()
      print("The file is converted.")

def save_results(folder_name, files_list):
      if os.path.exists(output_folder) is False:
            os.mkdir(output_folder)
      for i in files_list:
            shutil.copy2(folder_name + "/" + i, output_folder)
            convert(output_folder+ "/" + i)
            os.remove(output_folder+ "/" + i)

save_results(input_folder, collect_files(input_folder))
