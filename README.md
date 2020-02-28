#ENotiPy

###Description
Notipy is a simple script that emails the users upon code completion or failure.

###Environment Setup
ENotipy requires 4 environment variables to be setup prior to use. These variables
can be set 3 different ways. The first is manually. For a bash shell this would
look something like:

```
export ENOTIPY_EMAIL="dev.notipy@gmail.com"
export ENOTIPY_KEY="SuperSecretPassword"
export ENOTIPY_SMTP="smtp.gmail.com"
export ENOTIPY_PORT="587"
```

The next way is the info file. These commands can also be placed in a file like
the SAMPLE_INFO file provided and passed to the `infoFileEnvSetup(./SAMPLE_INFO)`
function in a script or using `-i=SAMPLE_INFO` as a command line argument.

The final way is to request environment setup prompts. This can be done with
`requestEnvSetup()` in a script or `-r=True` on the command line.

For examples of these options, checkout `scriptExample` and `codeExample.py`
Note that to use strictly "enotipy" on the commandline that the package must be installed. Otherwise, replace "enotipy" with "python /path/to/enotipy.py".
