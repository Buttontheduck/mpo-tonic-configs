import hydra
from omegaconf import OmegaConf
from tonic.train import train  # updated import

@hydra.main(config_path="/Users/batin13/Desktop/KIT/MPO/new_tonic/configs", config_name="config")
def main(cfg):
    print(OmegaConf.to_yaml(cfg))
    train(**cfg)

if __name__ == "__main__":
    main()
 