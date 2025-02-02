from llm_batch_processor.processor import BatchProcessor

def main():
    """Entry point for CLI"""
    processor = BatchProcessor()
    processor.process_csv()

if __name__ == "__main__":
    main()