import { Example } from "./Example";

import styles from "./Example.module.css";

export type ExampleModel = {
    text: string;
    value: string;
};

const EXAMPLES: ExampleModel[] = [
    {
        text: "What advanced functionality does the GitHub Enterprise Cloud add to github.com?",
        value: "What advanced functionality does the GitHub Enterprise Cloud add to github.com?"
    },
    { text: "What actions can Enterprise Owners take?", value: "What actions can Enterprise Owners take?" },
    { text: "How do I verify or approve a domain in my organization?", value: "How do I verify or approve a domain in my organization?" }
];

interface Props {
    onExampleClicked: (value: string) => void;
}

export const ExampleList = ({ onExampleClicked }: Props) => {
    return (
        <ul className={styles.examplesNavList}>
            {EXAMPLES.map((x, i) => (
                <li key={i}>
                    <Example text={x.text} value={x.value} onClick={onExampleClicked} />
                </li>
            ))}
        </ul>
    );
};
