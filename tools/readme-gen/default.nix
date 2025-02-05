{
  python3Packages,
  ...
}: python3Packages.buildPythonApplication rec {
  pname = "readme-gen";
  version = "1.0.0";
  pyproject = false;
  dontUnpack = true;

  installPhase = ''
    install -Dm 755 ${./${pname}.py} $out/bin/${pname}
  '';
}
