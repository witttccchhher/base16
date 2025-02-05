{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }: let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
  in {
    packages.${system} = {
      base16-preview = pkgs.callPackage ./default.nix { };
      default = self.packages.${system}.base16-preview;
    };
  };
}
