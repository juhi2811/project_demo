import argparse
from data_prep.prep_data import prepare_write_data
from model.train_model import train_model

def parse_args() -> argparse.Namespace:
   parser = argparse.ArgumentParser(description="Project Demo")

   parser.add_argument(
         "--dataset_path",
         type=str,
         required=True,
         help="""
            The path of dataset for model training.
         """,
      )
   parser.add_argument(
         "--model_path",
         type=str,
         required=True,
         help="""
            Path to save trained model.
         """,
      )
   parser.add_argument(
         "--metrics_path",
         type=str,
         required=True,
         help="""
            Path to save model metrics.
         """,
      )
   return parser.parse_args()


def run(dataset_path: str, model_path: str, metrics_path: str) -> None:
   if dataset_path.exists():
      print(f"Dataset already exists at {dataset_path}")
   else:
      prepare_write_data(dataset_path)
      print(f"Dataset created at {dataset_path}")

   train_model(dataset_path, model_path, metrics_path)
   print(f"Model trained and saved at {model_path}")
 


if __name__ == "__main__":
   parser = argparse.ArgumentParser(description="Project Demo")
   parser.add_argument("--dataset_path", type=str, required=True)
   parser.add_argument("--model_path", type=str, required=True)
   parser.add_argument("--metrics_path", type=str, required=True)

   args = parser.parse_args()
   run(args.dataset_path, args.model_path, args.metrics_path)
