module.exports = function (grunt) {
    var path=require('path');
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        project:path.basename(path.resolve()),
        banner: '/*!\n * <%= project %>\n' +
            ' * Author:<%= pkg.author %>\n' +
            ' * Summary:<%= pkg.description %>\n  */\n' ,
//            ' * License:<%= pkg.license %>\n' +
//            ' * Version: <%= pkg.version %>\n' +
//            ' *\n * URL:\n * <%= pkg.homepage %>\n' +
//            ' * <%= pkg.homepage %>/blob/master/LICENSE\n *\n */\n',

        less: {

  production: {
    options: {
      paths: ["assets/css"],
      cleancss: true
    },
    files: {
      "assets/css/style.min.css": "assets/css/main.css"
    }
  }
},
        uglify: {
            options: {
                banner: '<%= banner %>',
                compress: {
                    drop_console: true
                }
            },
            production: {
                files: {
                    'assets/js/main.min.js': ['assets/js/plugins.js','assets/js/main.js']
                }
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.registerTask('default', ['less:production','uglify:production']);

};